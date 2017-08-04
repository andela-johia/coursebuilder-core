const gulp = require('gulp'),
      scss = require('gulp-sass'),
      autoprefixer = require('gulp-autoprefixer');

gulp.task('scss', () => {
  gulp.src('scss/*.scss')
  .pipe(scss({outputStyle: 'compressed'}).on('error', scss.logError))
  .pipe(autoprefixer())
  .pipe(gulp.dest('css'));
});

gulp.task('watch', () => {
  gulp.watch('scss/**/*.scss', ['scss']);
});

gulp.task('default', ['scss', 'watch']);
