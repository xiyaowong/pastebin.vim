import os
import re

import requests

PASTE_UBUNTU_COM_SUPPORTED_SYNTAX = [
    'text',
    'abap',
    'abnf',
    'ada',
    'adl',
    'agda',
    'aheui',
    'ahk',
    'alloy',
    'ampl',
    'antlr',
    'antlr-as',
    'antlr-cpp',
    'antlr-csharp',
    'antlr-java',
    'antlr-objc',
    'antlr-perl',
    'antlr-python',
    'antlr-ruby',
    'apacheconf',
    'apl',
    'applescript',
    'arduino',
    'as',
    'as3',
    'aspectj',
    'aspx-cs',
    'aspx-vb',
    'asy',
    'at',
    'autoit',
    'awk',
    'basemake',
    'bash',
    'bat',
    'bbcode',
    'bc',
    'befunge',
    'bib',
    'blitzbasic',
    'blitzmax',
    'bnf',
    'boo',
    'boogie',
    'bro',
    'bst',
    'bugs',
    'c',
    'c-objdump',
    'ca65',
    'cadl',
    'camkes',
    'capdl',
    'capnp',
    'cbmbas',
    'ceylon',
    'cfc',
    'cfengine3',
    'cfm',
    'cfs',
    'chai',
    'chapel',
    'cheetah',
    'cirru',
    'clay',
    'clean',
    'clojure',
    'clojurescript',
    'cmake',
    'cobol',
    'cobolfree',
    'coffee-script',
    'common-lisp',
    'componentpascal',
    'console',
    'control',
    'coq',
    'cpp',
    'cpp-objdump',
    'cpsa',
    'cr',
    'crmsh',
    'croc',
    'cryptol',
    'csharp',
    'csound',
    'csound-document',
    'csound-score',
    'css',
    'css+django',
    'css+erb',
    'css+genshitext',
    'css+lasso',
    'css+mako',
    'css+mozpreproc',
    'css+myghty',
    'css+php',
    'css+smarty',
    'cucumber',
    'cuda',
    'cypher',
    'cython',
    'd',
    'd-objdump',
    'dart',
    'delphi',
    'dg',
    'diff',
    'django',
    'docker',
    'doscon',
    'dpatch',
    'dtd',
    'duel',
    'dylan',
    'dylan-console',
    'dylan-lid',
    'earl-grey',
    'easytrieve',
    'ebnf',
    'ec',
    'ecl',
    'eiffel',
    'elixir',
    'elm',
    'emacs',
    'erb',
    'erl',
    'erlang',
    'evoque',
    'extempore',
    'ezhil',
    'factor',
    'fan',
    'fancy',
    'felix',
    'fish',
    'flatline',
    'forth',
    'fortran',
    'fortranfixed',
    'foxpro',
    'fsharp',
    'gap',
    'gas',
    'genshi',
    'genshitext',
    'glsl',
    'gnuplot',
    'go',
    'golo',
    'gooddata-cl',
    'gosu',
    'groff',
    'groovy',
    'gst',
    'haml',
    'handlebars',
    'haskell',
    'haxeml',
    'hexdump',
    'hsail',
    'html',
    'html+cheetah',
    'html+django',
    'html+evoque',
    'html+genshi',
    'html+handlebars',
    'html+lasso',
    'html+mako',
    'html+myghty',
    'html+ng2',
    'html+php',
    'html+smarty',
    'html+twig',
    'html+velocity',
    'http',
    'hx',
    'hybris',
    'hylang',
    'i6t',
    'idl',
    'idris',
    'iex',
    'igor',
    'inform6',
    'inform7',
    'ini',
    'io',
    'ioke',
    'irc',
    'isabelle',
    'j',
    'jags',
    'jasmin',
    'java',
    'javascript+mozpreproc',
    'jcl',
    'jlcon',
    'js',
    'js+cheetah',
    'js+django',
    'js+erb',
    'js+genshitext',
    'js+lasso',
    'js+mako',
    'js+myghty',
    'js+php',
    'js+smarty',
    'jsgf',
    'json',
    'json-object',
    'jsonld',
    'jsp',
    'julia',
    'juttle',
    'kal',
    'kconfig',
    'koka',
    'kotlin',
    'lagda',
    'lasso',
    'lcry',
    'lean',
    'less',
    'lhs',
    'lidr',
    'lighty',
    'limbo',
    'liquid',
    'live-script',
    'llvm',
    'logos',
    'logtalk',
    'lsl',
    'lua',
    'make',
    'mako',
    'maql',
    'mask',
    'mason',
    'mathematica',
    'matlab',
    'matlabsession',
    'md',
    'minid',
    'modelica',
    'modula2',
    'monkey',
    'monte',
    'moocode',
    'moon',
    'mozhashpreproc',
    'mozpercentpreproc',
    'mql',
    'mscgen',
    'mupad',
    'mxml',
    'myghty',
    'mysql',
    'nasm',
    'ncl',
    'nemerle',
    'nesc',
    'newlisp',
    'newspeak',
    'ng2',
    'nginx',
    'nim',
    'nit',
    'nixos',
    'nsis',
    'numpy',
    'nusmv',
    'objdump',
    'objdump-nasm',
    'objective-c',
    'objective-c++',
    'objective-j',
    'ocaml',
    'octave',
    'odin',
    'ooc',
    'opa',
    'openedge',
    'pacmanconf',
    'pan',
    'parasail',
    'pawn',
    'perl',
    'perl6',
    'php',
    'pig',
    'pike',
    'pkgconfig',
    'plpgsql',
    'postgresql',
    'postscript',
    'pot',
    'pov',
    'powershell',
    'praat',
    'prolog',
    'properties',
    'protobuf',
    'ps1con',
    'psql',
    'pug',
    'puppet',
    'py3tb',
    'pycon',
    'pypylog',
    'pytb',
    'python',
    'python3',
    'qbasic',
    'qml',
    'qvto',
    'racket',
    'ragel',
    'ragel-c',
    'ragel-cpp',
    'ragel-d',
    'ragel-em',
    'ragel-java',
    'ragel-objc',
    'ragel-ruby',
    'raw',
    'rb',
    'rbcon',
    'rconsole',
    'rd',
    'rebol',
    'red',
    'redcode',
    'registry',
    'resource',
    'rexx',
    'rhtml',
    'rnc',
    'roboconf-graph',
    'roboconf-instances',
    'robotframework',
    'rql',
    'rsl',
    'rst',
    'rts',
    'rust',
    'sas',
    'sass',
    'sc',
    'scala',
    'scaml',
    'scheme',
    'scilab',
    'scss',
    'shen',
    'silver',
    'slim',
    'smali',
    'smalltalk',
    'smarty',
    'sml',
    'snobol',
    'snowball',
    'sourceslist',
    'sp',
    'sparql',
    'spec',
    'splus',
    'sql',
    'sqlite3',
    'squidconf',
    'ssp',
    'stan',
    'stata',
    'swift',
    'swig',
    'systemverilog',
    'tads3',
    'tap',
    'tasm',
    'tcl',
    'tcsh',
    'tcshcon',
    'tea',
    'termcap',
    'terminfo',
    'terraform',
    'tex',
    'text',
    'thrift',
    'todotxt',
    'trac-wiki',
    'treetop',
    'ts',
    'tsql',
    'turtle',
    'twig',
    'typoscript',
    'typoscriptcssdata',
    'typoscripthtmldata',
    'urbiscript',
    'vala',
    'vb.net',
    'vcl',
    'vclsnippets',
    'vctreestatus',
    'velocity',
    'verilog',
    'vgl',
    'vhdl',
    'vim',
    'wdiff',
    'whiley',
    'x10',
    'xml',
    'xml+cheetah',
    'xml+django',
    'xml+erb',
    'xml+evoque',
    'xml+lasso',
    'xml+mako',
    'xml+myghty',
    'xml+php',
    'xml+smarty',
    'xml+velocity',
    'xquery',
    'xslt',
    'xtend',
    'xul+mozpreproc',
    'yaml',
    'yaml+jinja',
    'zephir',
]


def paste_ubuntu_com(
    content: str, syntax: str = '', expiration: str = ''
) -> (str, bool):
    """for paste.ubuntu.com

    :param author: poster
    :param syntax: filetype
    :param expiration:  "" => nerver expire
                        "day" => a day
                        "week" => a week
                        "month" => a month
                        "year" => a year
    :param content: the text to paste
    """
    data = {
        "poster": os.environ.get('USER', 'anonymous'),
        "syntax": syntax if syntax in PASTE_UBUNTU_COM_SUPPORTED_SYNTAX else 'text',
        "content": content,
        "expiration": expiration
        if expiration in ['', 'day', 'week', 'month', 'year']
        else '',
    }
    try:
        resp = requests.post(
            "https://paste.ubuntu.com/",
            data=data,
            timeout=5,
        )
        resp.raise_for_status()
    except Exception as e:
        return str(e), False
    else:
        link = re.findall(r'<a class="pturl" href="/p/(\w+)/plain/">', resp.text)
        if link:
            return "https://paste.ubuntu.com/p/%s/" % link[0], True
        return "Paste failed.", False
