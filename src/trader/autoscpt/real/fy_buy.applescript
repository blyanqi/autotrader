-- tell block to fy buy
on run argv
    set Code to item 1 of argv
    set Num to item 2 of argv
    tell application "Keyboard Maestro Engine" 
        activate
        do script "378CB5C9-DF84-4D40-AFE0-32D6019E5345" with parameter Code & ", " & Num
    end tell
end run