# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests that walk through Course Builder pages."""

__author__ = 'Sean Lip'

import json
import os
import urllib

from controllers import sites
from controllers import utils
from controllers.sites import assert_fails
from models import models
from models.utils import get_all_scores
from models.utils import get_answer
from models.utils import get_score
from modules.announcements.announcements import AnnouncementEntity

import actions
from actions import assert_contains
from actions import assert_does_not_contain
from actions import assert_equals


class AdminAspectTest(actions.TestBase):
    """Tests site from the Admin perspective."""

    def test_admin_list(self):
        """Test delegation of admin access to another user."""

        email = 'test_admin_list@google.com'
        actions.login(email)

        # Check user has no access.
        response = self.testapp.get('/admin?action=settings')
        assert_equals(response.status_int, 302)

        # Add override.
        os.environ['gcb_admin_list'] = email

        # Check user has access now.
        response = self.testapp.get('/admin?action=settings')
        assert_equals(response.status_int, 200)
        assert_contains('gcb_admin_list', response.body)
        assert_contains('test_admin_list@google.com', response.body)
        assert_contains(
            '/admin?action=config_edit&name=gcb_admin_list', response.body)
        assert_contains(
            '/admin?action=config_reset&name=gcb_admin_list', response.body)

        # Remove override.
        del os.environ['gcb_admin_list']

        # Check user has no access.
        response = self.testapp.get('/admin?action=settings')
        assert_equals(response.status_int, 302)

    def test_access_to_admin_pages(self):
        """Test access to admin pages."""

        # assert anonymous user has no access
        response = self.testapp.get('/admin?action=settings')
        assert_equals(response.status_int, 302)

        # assert admin user has access
        email = 'test_access_to_admin_pages@google.com'
        name = 'Test Access to Admin Pages'

        actions.login(email, True)
        actions.register(self, name)

        response = self.testapp.get('/admin')
        assert_contains('Power Searching with Google', response.body)
        assert_contains('All Courses', response.body)

        response = self.testapp.get('/admin?action=settings')
        assert_contains('gcb_admin_list', response.body)
        assert_contains('gcb_config_update_interval_sec', response.body)
        assert_contains('All Settings', response.body)

        response = self.testapp.get('/admin?action=perf')
        assert_contains('gcb-admin-uptime-sec:', response.body)
        assert_contains('In-process Performance Counters', response.body)

        response = self.testapp.get('/admin?action=deployment')
        assert_contains('application_id: testbed-test', response.body)
        assert_contains('Application Identity', response.body)

        actions.unregister(self)
        actions.logout()

        # assert not-admin user has no access
        actions.login(email)
        actions.register(self, name)
        response = self.testapp.get('/admin?action=settings')
        assert_equals(response.status_int, 302)

    def test_multiple_courses(self):
        """Tests courses admin page with two courses configured."""

        config = 'course:/foo:/foo-data, course:/bar:/bar-data'
        os.environ[sites.GCB_COURSES_CONFIG_ENV_VAR_NAME] = config

        email = 'test_multiple_courses@google.com'

        actions.login(email, True)
        response = self.testapp.get('/admin')
        assert_contains('Course Builder - Courses', response.body)
        assert_contains('<a href="/foo">', response.body)
        assert_contains('/foo-data', response.body)
        assert_contains('<a href="/bar">', response.body)
        assert_contains('/bar-data', response.body)
        assert_contains('Total: 2 item(s)', response.body)

        del os.environ[sites.GCB_COURSES_CONFIG_ENV_VAR_NAME]


class CourseAuthorAspectTest(actions.TestBase):
    """Tests the site from the Course Author perspective."""

    def test_draft_announcements(self):
        """Test course author can see draft announcements."""
        email = 'test_announcements@google.com'
        name = 'Test Announcements'

        actions.login(email, True)
        actions.register(self, name)

        response = actions.view_announcements(self)
        assert_contains('Welcome to the final class!', response.body)

    def test_manage_announcements(self):
        """Test course author can manage announcements."""
        email = 'test_announcements@google.com'
        name = 'Test Announcements'

        actions.login(email, True)
        actions.register(self, name)

        # add new
        response = actions.view_announcements(self)
        add_form = response.forms['gcb-add-announcement']
        response = self.submit(add_form)
        assert_equals(response.status_int, 302)

        # check added
        response = actions.view_announcements(self)
        assert_contains('Sample Announcement (Draft)', response.body)

        # delete draft
        response = actions.view_announcements(self)
        delete_form = response.forms['gcb-delete-announcement-1']
        response = self.submit(delete_form)
        assert_equals(response.status_int, 302)

        # check deleted
        assert_does_not_contain('Welcome to the final class!', response.body)

    def test_announcements_rest(self):
        """Test REST access to announcements."""
        email = 'test_announcements_rest@google.com'
        name = 'Test Announcements Rest'

        actions.login(email, True)
        actions.register(self, name)

        response = actions.view_announcements(self)
        assert_does_not_contain('My Test Title', response.body)

        # REST GET existing item
        items = AnnouncementEntity.all().fetch(1)
        for item in items:
            response = self.get('rest/announcements/item?key=%s' % item.key())
            json_dict = json.loads(response.body)
            assert json_dict['status'] == 200
            assert 'message' in json_dict
            assert 'payload' in json_dict

            payload_dict = json.loads(json_dict['payload'])
            assert 'title' in payload_dict
            assert 'date' in payload_dict

            # REST PUT item
            payload_dict['title'] = 'My Test Title'
            payload_dict['date'] = '2012/12/31'
            payload_dict['is_draft'] = True
            request = {}
            request['key'] = str(item.key())
            request['payload'] = json.dumps(payload_dict)
            response = self.put('rest/announcements/item?%s' % urllib.urlencode(
                {'request': json.dumps(request)}), {})

            # confirm change is visible
            response = self.get('announcements')
            assert_contains('My Test Title (Draft)', response.body)

        # REST GET not-existing item
        response = self.get('rest/announcements/item?key=not_existent_key')
        json_dict = json.loads(response.body)
        assert json_dict['status'] == 404


class StudentAspectTest(actions.TestBase):
    """Tests the site from the Student perspective."""

    def test_draft_announcements(self):
        """Test student can't see draft announcements."""
        email = 'test_draft_announcements@google.com'
        name = 'Test Draft Announcements'

        actions.login(email)
        actions.register(self, name)

        response = actions.view_announcements(self)
        assert_does_not_contain('Welcome to the final class!', response.body)

    def test_registration(self):
        """Test student registration."""
        email = 'test_registration@example.com'
        name1 = 'Test Student'
        name2 = 'John Smith'
        name3 = 'Pavel Simakov'

        actions.login(email)

        actions.register(self, name1)
        actions.check_profile(self, name1)

        actions.change_name(self, name2)
        actions.unregister(self)

        actions.register(self, name3)
        actions.check_profile(self, name3)

    def test_limited_class_size_registration(self):
        """Test student registration with MAX_CLASS_SIZE."""
        utils.MAX_CLASS_SIZE = 2

        email1 = '111@example.com'
        name1 = 'student1'
        email2 = '222@example.com'
        name2 = 'student2'
        email3 = '333@example.com'
        name3 = 'student3'

        actions.login(email1)
        actions.register(self, name1)
        actions.logout()

        actions.login(email2)
        actions.register(self, name2)
        actions.logout()

        actions.login(email3)
        assert_fails(lambda: actions.register(self, name3))
        actions.logout()

        # Now unset the limit, and registration should succeed
        utils.MAX_CLASS_SIZE = None
        actions.login(email3)
        actions.register(self, name3)
        actions.logout()

    def test_permissions(self):
        """Test student permissions, and which pages they can view."""
        email = 'test_permissions@example.com'
        name = 'Test Permissions'

        actions.login(email)

        actions.register(self, name)
        actions.Permissions.assert_enrolled(self)

        actions.unregister(self)
        actions.Permissions.assert_unenrolled(self)

        actions.register(self, name)
        actions.Permissions.assert_enrolled(self)

    def test_login_and_logout(self):
        """Test if login and logout behave as expected."""
        email = 'test_login_logout@example.com'

        actions.Permissions.assert_logged_out(self)
        actions.login(email)

        actions.Permissions.assert_unenrolled(self)

        actions.logout()
        actions.Permissions.assert_logged_out(self)


class PageCacheTest(actions.TestBase):
    """Checks if pages cached for one user are properly render for another."""

    def test_page_cache(self):
        """Test a user can't see other user pages."""
        email1 = 'user1@foo.com'
        name1 = 'User 1'
        email2 = 'user2@foo.com'
        name2 = 'User 2'

        # Login as one user and view 'unit' and other pages, which are not
        # cached.
        actions.login(email1)
        actions.register(self, name1)
        actions.Permissions.assert_enrolled(self)
        response = actions.view_unit(self)
        assert_contains(email1, response.body)
        actions.logout()

        # Login as another user and check that 'unit' and other pages show
        # the correct new email.
        actions.login(email2)
        actions.register(self, name2)
        actions.Permissions.assert_enrolled(self)
        response = actions.view_unit(self)
        assert_contains(email2, response.body)
        actions.logout()


class AssessmentTest(actions.TestBase):
    """Tests for assessments."""

    def submit_assessment(self, name, args):
        response = self.get('assessment?name=%s' % name)
        assert_contains(
            '<script src="assets/js/assessment-%s.js"></script>' % name,
            response.body)
        response = self.post('answer', args)
        assert_equals(response.status_int, 200)
        return response

    def test_course_pass(self):
        """Tests student passing final exam."""
        email = 'test_pass@google.com'
        name = 'Test Pass'

        post = {'assessment_type': 'postcourse',
                'num_correct': '0', 'num_questions': '4',
                'score': '100.00'}

        # Register.
        actions.login(email)
        actions.register(self, name)

        # Submit answer.
        response = self.submit_assessment('Post', post)
        assert_equals(response.status_int, 200)
        assert_contains('Your score is 70%', response.body)
        assert_contains('you have passed the course', response.body)

        # Check that the result shows up on the profile page.
        response = actions.check_profile(self, name)
        assert_contains('70', response.body)
        assert_contains('100', response.body)

    def test_assessments(self):
        """Tests assessment scores are properly submitted and summarized."""
        email = 'test_assessments@google.com'
        name = 'Test Assessments'

        pre = {'assessment_type': 'precourse',
               '0': 'false', '1': 'false', '2': 'false', '3': 'false',
               'num_correct': '0', 'num_questions': '4',
               'score': '1.00'}

        mid = {'assessment_type': 'midcourse',
               '0': 'false', '1': 'false', '2': 'false', '3': 'false',
               'num_correct': '0', 'num_questions': '4',
               'score': '2.00'}

        post = {'assessment_type': 'postcourse',
                '0': 'false', '1': 'false', '2': 'false', '3': 'false',
                'num_correct': '0', 'num_questions': '4',
                'score': '3.00'}

        second_mid = {'assessment_type': 'midcourse',
                      '0': 'false', '1': 'false', '2': 'false', '3': 'false',
                      'num_correct': '0', 'num_questions': '4',
                      'score': '1.00'}

        second_post = {'assessment_type': 'postcourse',
                       '0': 'false', '1': 'false', '2': 'false', '3': 'false',
                       'num_correct': '0', 'num_questions': '4',
                       'score': '100000'}

        # Register.
        actions.login(email)
        actions.register(self, name)

        # Check that no scores exist right now.
        student = models.Student.get_enrolled_student_by_email(email)
        assert len(get_all_scores(student)) == 0  # pylint: disable=C6411

        # Submit assessments and check the numbers of scores recorded.
        self.submit_assessment('Pre', pre)
        student = models.Student.get_enrolled_student_by_email(email)
        assert len(get_all_scores(student)) == 1

        self.submit_assessment('Mid', mid)
        student = models.Student.get_enrolled_student_by_email(email)
        assert len(get_all_scores(student)) == 2

        self.submit_assessment('Post', post)
        student = models.Student.get_enrolled_student_by_email(email)
        assert len(get_all_scores(student)) == 4  # also includes overall_score

        assert isinstance(get_answer(student, 'precourse'), list)
        assert isinstance(get_answer(student, 'midcourse'), list)
        assert isinstance(get_answer(student, 'postcourse'), list)

        # Check that scores are recorded properly.
        student = models.Student.get_enrolled_student_by_email(email)
        assert int(get_score(student, 'precourse')) == 1
        assert int(get_score(student, 'midcourse')) == 2
        assert int(get_score(student, 'postcourse')) == 3
        assert (int(get_score(student, 'overall_score')) ==
                int((0.30 * 2) + (0.70 * 3)))

        # Try posting a new midcourse exam with a lower score; nothing should
        # change.
        self.submit_assessment('Mid', second_mid)
        student = models.Student.get_enrolled_student_by_email(email)
        assert int(get_score(student, 'precourse')) == 1
        assert int(get_score(student, 'midcourse')) == 2
        assert int(get_score(student, 'postcourse')) == 3
        assert (int(get_score(student, 'overall_score')) ==
                int((0.30 * 2) + (0.70 * 3)))

        # Now try posting a postcourse exam with a higher score and note
        # the changes.
        self.submit_assessment('Post', second_post)
        student = models.Student.get_enrolled_student_by_email(email)
        assert int(get_score(student, 'precourse')) == 1
        assert int(get_score(student, 'midcourse')) == 2
        assert int(get_score(student, 'postcourse')) == 100000
        assert (int(get_score(student, 'overall_score')) ==
                int((0.30 * 2) + (0.70 * 100000)))


class CourseUrlRewritingTest(
    StudentAspectTest, PageCacheTest, AssessmentTest, CourseAuthorAspectTest,
    AdminAspectTest):
    """Runs existing tests using rewrite rules for '/courses/pswg' base URL."""

    def setUp(self):  # pylint: disable-msg=g-bad-name
        self.base = '/courses/pswg'
        self.namespace = 'gcb-courses-pswg-tests-ns'

        config = 'course:%s:/:%s' % (self.base, self.namespace)
        os.environ[sites.GCB_COURSES_CONFIG_ENV_VAR_NAME] = config

        super(CourseUrlRewritingTest, self).setUp()

    def tearDown(self):  # pylint: disable-msg=g-bad-name
        super(CourseUrlRewritingTest, self).tearDown()
        del os.environ[sites.GCB_COURSES_CONFIG_ENV_VAR_NAME]

    def canonicalize(self, href, response=None):
        """Canonicalize URL's using either <base> or self.base."""
        # Check if already canonicalized.
        if href.startswith(self.base):
            return href

        # Look for <base> tag in the response to compute the canonical URL.
        if response:
            return super(CourseUrlRewritingTest, self).canonicalize(
                href, response)

        # Prepend self.base to compute the canonical URL.
        if not href.startswith('/'):
            href = '/%s' % href
        href = '%s%s' % (self.base, href)
        return href
