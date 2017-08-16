const gulp = require('gulp'),
  scss = require('gulp-sass'),
  autoprefixer = require('gulp-autoprefixer'),
  babel = require('gulp-babel');

gulp.task('scss', () => {
  gulp.src('scss/*.scss')
  .pipe(scss({ outputStyle: 'compressed' }).on('error', scss.logError))
  .pipe(autoprefixer())
  .pipe(gulp.dest('css'))
  .pipe(gulp.dest('../coursebuilder/modules/explorer/_static/css'));
});

gulp.task('watch', () => {
  gulp.watch('scss/**/*.scss', ['scss']);
  gulp.watch('js-source/*.js', ['babel']);
});

gulp.task('default', ['scss', 'babel', 'watch']);

gulp.task('babel', () =>
    gulp.src('js-source/main.js')
        .pipe(babel({ presets: ['es2015-script'] }))
        .pipe(gulp.dest('js'))
        .pipe(gulp.dest('../coursebuilder/modules/explorer/_static/js'))
);
