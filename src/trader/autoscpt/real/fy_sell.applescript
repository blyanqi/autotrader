-- tell block to fy sell
on run argv
    set Code to item 1 of argv
    set Num to item 2 of argv
    tell application "Keyboard Maestro Engine" 
        activate
        do script "12FA5AFA-3013-464B-90B3-9D8DCB98AF21" with parameter Code & ", " & Num
    end tell
end run