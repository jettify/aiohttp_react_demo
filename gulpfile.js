'use strict';

// requirements

var gulp = require('gulp'),
    browserify = require('gulp-browserify'),
    size = require('gulp-size'),
    clean = require('gulp-clean');


// tasks

gulp.task('transform', function () {
  return gulp.src('./aiohttp_demo_react/static/scripts/jsx/main.js')
    .pipe(browserify({transform: ['reactify']}))
    .pipe(gulp.dest('./aiohttp_demo_react/static/scripts/js'))
    .pipe(size());
});

gulp.task('clean', function () {
  return gulp.src(['./aiohttp_demo_react/static/scripts/js'], {read: false})
    .pipe(clean());
});

gulp.task('default', ['clean'], function () {
  gulp.start('transform');
  gulp.watch('./aiohttp_demo_react/static/scripts/jsx/main.js', ['transform']);
});