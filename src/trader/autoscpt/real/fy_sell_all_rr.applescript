-- tell block to fy sell
on run argv
    set Code to item 1 of argv
    tell application "Keyboard Maestro Engine" 
        -- activate
        do script "2230482C-98F9-45AF-BB9E-5DCE89D6C046" with parameter Code
    end tell
end run