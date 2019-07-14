from invoke import task
from plumbum import local
from shutil import copyfile
from pathlib import *

import filecmp
import os
import json

#from pi_autolib import *

template_path = Path('theme/templates/')
css_path = Path('static/css/')

# Paths
# ------------------------------------------------------------------------------
content_path = Path("./content")
theme_path = Path("./theme")
preview_path = Path("./preview")
production_path = Path("./production")

template_path = Path('templates')
css_path = Path('static/css')
scss_path = Path('static/scss')


# Global Variables
# ------------------------------------------------------------------------------
ruby = local['ruby']
python = local["python"]
pelican = local["pelican"]

sass_path = Path('C:/msys64/home/Monthy/.gem/ruby/2.1.0/bin/sass')


# Tasks
# ------------------------------------------------------------------------------
@task
def compile_scss(ctx, theme='rubber-squid', verbose=False ):
    if verbose:
        print("Compiling scss")

    path = theme_path / Path(theme)
    for entry in (path / scss_path).glob('*.scss'):
        if verbose:
            print("  Compiling: {} ...".format(entry.name), end='')

        target_path = path / css_path / Path(entry.name).with_suffix(".css")

        if not (target_path.parent.exists() and target_path.parent.is_dir()):
            target_path.parent.mkdir()
        ruby(str(sass_path), str(entry), str(target_path))

        if verbose:
            print("[DONE]")


@task
def compile(ctx,
            verbose=False,
            target="preview"):
    if target == "preview":
        conf = "pelicanconf.py"
    elif target == "production":
        conf = "publishconf.py"
    else:
        raise Exception()

    pelican("content", "-s", conf)


@task
def preview(ctx, verbose=False, target="preview"):
    if verbose:
        print("Running http server for {}".format(target))

    cwd = Path.cwd()
    os.chdir(str(Path("./{}/".format(target))))
    python("-m", "http.server") & FG
    os.chdir(str(cwd))

