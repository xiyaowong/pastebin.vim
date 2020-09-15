if has('python3')

function! Pastebin() 
python3 << EOF
import sys
import vim
sys.path.append(vim.eval('expand("<sfile>:h")'))
from pastebin import paste_ubuntu_com

filetype = vim.eval('&filetype')
content=os.linesep.join(list(vim.current.buffer))
link, _ = paste_ubuntu_com(syntax=filetype, content=content, expiration='month')
print(link)
EOF
endfunction

command! -nargs=0 Pastebin call Pastebin()
endif
