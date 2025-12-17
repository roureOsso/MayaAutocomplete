
## What is MayaAutocomplete?
**MayaAutocomplete** is simple python script that will parse the official Maya documentation to generate a new `__init__.pyi` for you to use as autocomplete.<br />
- You should not need to build your own autoComplete therefore I will not add details about how to use the script. If you know what you are looking at I hope it is self-explanatory enough. Tested for windows and py3.x

**MayaAutocomplete** is also a library with already generated autoCompletes for the different Maya major versions. You don't need to run any python script if you do not want or need to.<br />

Thx to [Enrique Velasco](https://github.com/enriquevelmai) who originally told me about the idea.


## Auto Complete Usage  
From the [releases tab](https://github.com/roureOsso/MayaAutocomplete/releases) is this page you will be able to download you desired `autoCompleteMaya{version}.zip`<br />

Once unzipped you should see the following files/dirs:<br />
<pre>
autoCompleteMaya{version}
|__ maya-stubs
    |__ __init__.pyi
    |__ cmds
        |__ __init__.pyi
</pre>

This files configuration follow [PEP 561](https://peps.python.org/pep-0561/) for stubs. Therefore, now you can add `autoCompleteMaya{version}` to your interpreter python paths without shadowing the "real" Maya directories.<br />
Go to the [releases tab](https://github.com/roureOsso/MayaAutocomplete/releases) for a video example on how to do that with pycharm.
