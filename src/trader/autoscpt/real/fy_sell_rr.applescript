-- tell block to fy sell
on run argv
    set Code to item 1 of argv
    set Num to item 2 of argv
    tell application "Keyboard Maestro Engine" 
        -- activate
        do script "85E5FFAA-B4EE-42C0-B43E-7B6B1D1095FA" with parameter Code & ", " & Num
    end tell
end run