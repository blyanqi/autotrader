-- tell block to fy buy
on run argv
    set Code to item 1 of argv
    set Num to item 2 of argv
    tell application "Keyboard Maestro Engine" 
        -- activate
        do script "848C64D9-A69C-4C4B-B345-CB47E074D97C" with parameter Code & ", " & Num
    end tell
end run