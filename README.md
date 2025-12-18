
## What is MayaAutocomplete?
Until Autodesk ended support for PyMel, a series of stub files were provided to be used for 'autoComplete' in our editors. 
However, even then, when using a 'cmds' command, the available flags were not suggested.

This project was created to generate a more comprehensive stub file with argument suggestions.

Now that Autodesk has officially stopped providing these files following the end of PyMel support, this project will also 
include a copy of the latest stub files for those interested in having a basic autocomplete for the rest of the API commands.

Please note, however, that unlike the 'cmds' implementation, generating a more complete version for these other commands 
is not part of this project's objective (for now at least).

**MayaAutocomplete** is a simple python script that will parse the official Maya documentation to generate a new 
`__init__.pyi` for you to use as autocomplete.<br />

**MayaAutocomplete** is also a library with already generated autoCompletes for the different Maya major versions. 
You don't need to run any python script if you do not want or need to, just download what you need.<br />

Thanks to [Enrique Velasco](https://github.com/enriquevelmai) who originally told me about the ideaon how to do that.


## Auto Complete Usage  
From the [releases tab](https://github.com/roureOsso/MayaAutocomplete/releases) you will be able to download your desired `autoCompleteMaya{version}.zip`<br />

Once unzipped you should see the following files/dirs:<br />
<pre>
autoCompleteMaya{version}
|__ maya-stubs
    |__ __init__.pyi
    |__ cmds
        |__ __init__.pyi
    |__ api
    |__ OpenMaya.pyi
    |__ ...
</pre>

This files configuration follow the [PEP 561](https://peps.python.org/pep-0561/) for stubs. Therefore, now you can add `autoCompleteMaya{version}` 
to your interpreter python paths without shadowing the "real" Maya directories.<br />

Go to the [releases tab](https://github.com/roureOsso/MayaAutocomplete/releases) for a video example on how to do that with pycharm.
