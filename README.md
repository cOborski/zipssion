<center>

# Zipssion
![version: 0.1.0-alpha](https://img.shields.io/badge/0.1.0-alpha?style=plastic&logoSize=auto&label=version&labelColor=black&color=blue&link=https%3A%2F%2Fsemver.org%2F) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Project Type: toy](https://img.shields.io/badge/project%20type-toy-blue)](https://project-types.github.io/#toy) [![ide: pulsar](https://87dx2k69x4yr.runkit.sh)](https://pulsar-edit.dev/)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FcOborski%2Fzipssion.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FcOborski%2Fzipssion?ref=badge_shield)
</center>

## What is this?
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=70A909&background=00000098&multiline=true&width=435&height=150&lines=Zipssion+is+a+command+line+program;that+aids+in+the+design+and;reverse+engineering+of+custom;file+types.)](https://git.io/typing-svg)

## More about this repository

This project is just getting started and only has a couple of features implemented! I intend to use semantic versioning for zipssion, but for now consider it to be version 0.1.0-alpha (a prerelease state.)

## Known issues / TODOs

- [ ] List out commands
- [ ] Generate documentation
- [ ] Write getting started guide
- [ ] Currently, zipssion is using [python-magic](https://github.com/ahupp/python-magic) (libmagic) for file identification but I want to add a flag that allows the user to use [Magika](https://github.com/google/magika) instead. (or maybe in addition to?)
- [ ] Write tests
- [ ] Continue writing TODOs...

## View source

[![cOborski/zipssion](https://img.shields.io/static/v1?label=cOborski&message=zipssion&color=yellow&logo=github)](https://github.com/coborski/zipssion/)

## Planned Usage (incomplete/wip)
```
Usage:
main.py <file> [--quiet | --verbose] [--path=<path>] [--extention=<file extention>]
main.py (-h | --help)
main.py --version
main.py --quiet
main.py --verbose

Options:
-h --help      show help text
--version      show version
--quiet        print less text
--verbose      print more text
--path=<path>  list of file paths [default: {'/'}]
--extention=<file extention>  the file's extention (if known)
```

## Credits, inspiration, and references

### Articles, guides, and resources
- [Command Line Interface Guidelines](https://clig.dev/)

### Libraries used by zipssion
- [Typer](https://typer.tiangolo.com/)
- [rich-cli](https://github.com/Textualize/rich-cli)
- [python-magic](https://github.com/ahupp/python-magic)

### Tools
- [Python Black](https://github.com/psf/black)
- [isort](https://github.com/PyCQA/isort)

### Fun things/Other
- [Readme Typing](https://readme-typing-svg.demolab.com/demo/)

### Things I'm saving for latter possible use
- [pyfiglet](https://github.com/pwaller/pyfiglet)
- [asciinema](https://asciinema.org/)
- [Magika](https://github.com/google/magika)

[🔝](#zipssion)


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FcOborski%2Fzipssion.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FcOborski%2Fzipssion?ref=badge_large)