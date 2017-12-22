# deoplete-sfservices
[Deoplete](https://github.com/Shougo/deoplete.nvim) plugin for symfony services. 
Provides service names completions in _PHP_ files. It searches for _./app/console_ 
or _./bin/console_ executable in current working directory, executes it with 
_debug:container_ parameter and puts result into completon sources. Works with 
_symfony_ 2, 3 and 4.

#### Installation (using [vim-plug](https://github.com/junegunn/vim-plug))

```vim
Plug 'Shougo/deoplete.nvim', {'do': ':UpdateRemotePlugins'}
Plug 'jvmanji/deoplete-sfservices'
```
