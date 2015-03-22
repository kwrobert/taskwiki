let s:plugin_path = escape(expand('<sfile>:p:h:h'), '\')
execute 'pyfile ' . s:plugin_path . '/taskwiki/taskwiki.py'

augroup taskwiki
    " when saving the file sync the tasks from vimwiki to TW
    autocmd!
    execute "autocmd BufWrite *.".expand('%:e')." py WholeBuffer.update_to_tw()"
augroup END

command! TaskWikiProjects :py Splits.projects()
command! TaskWikiProjectsSummary :py Splits.summary()
command! TaskWikiBurndown :py Splits.burndown()

command! -range TaskWikiInfo :<line1>,<line2>py SelectedTasks().info()
command! -range TaskWikiLink :<line1>,<line2>py SelectedTasks().link()
command! -range TaskWikiDelete :<line1>,<line2>py SelectedTasks().delete()
command! -range -nargs=* TaskWikiMod :<line1>,<line2>py SelectedTasks().modify(<q-args>)

" Disable <CR> as VimwikIFollowLink
if !hasmapto('<Plug>VimwikiFollowLink')
  nmap <Plug>NoVimwikiFollowLink <Plug>VimwikiFollowLink
endif

nmap <silent><buffer> <CR> :py Mappings.task_info_or_vimwiki_follow_link()<CR>