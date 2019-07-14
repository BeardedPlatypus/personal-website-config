var gulp = require('gulp');
var sass = require('gulp-sass');
var path = require('path');
var useref = require('gulp-useref');
var cssnano = require('gulp-cssnano');
var gulpIf = require('gulp-if');
var promisedDel = require('promised-del');
var runSequence = require('run-sequence');


var themePath = path.join('theme', 'rubber-squid');


var sassInPath = path.join(themePath, 'static', 'scss');
var cssOutPath = path.join(themePath, 'static', 'css');

gulp.task('sass', function() {
    return gulp.src( path.join(sassInPath, "**", "*.scss")
                   , { base: sassInPath } 
                   )
      .pipe(sass())
      .pipe(gulp.dest(cssOutPath))
});


var productionPreOptimisePath = path.join('production');
var productionPostOptimisePath = path.join('website_dist');

gulp.task('useref', function() {
    return gulp.src( path.join( productionPreOptimisePath, "**", "*.html" )
                   , { base: productionPreOptimisePath })
      .pipe(useref())
      .pipe(gulpIf('*.css', cssnano()))
      .pipe(gulp.dest(productionPostOptimisePath))
});


gulp.task('js', function() {
    return gulp.src(path.join(productionPreOptimisePath, "**", "*.js"), 
                    { base: productionPreOptimisePath })
      .pipe(gulp.dest(productionPostOptimisePath))
});


gulp.task('feeds', function() {
    return gulp.src(path.join(productionPreOptimisePath, "feeds", "*.xml"), 
                    { base: productionPreOptimisePath })
      .pipe(gulp.dest(productionPostOptimisePath))
})


gulp.task('clean:dist', function() {
    return promisedDel([productionPostOptimisePath]);
});


// Sequenced tasks
gulp.task('prePelican', gulp.series('sass', function(done) {
    done();
}));


gulp.task('postPelican', gulp.series('clean:dist', 'useref', 'js', 'feeds', function(done) {
    done();
}));