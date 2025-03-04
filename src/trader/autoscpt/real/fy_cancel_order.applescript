on run argv
    set Code to item 1 of argv
    tell application "Keyboard Maestro Engine" 
        activate
        do script "6115F26A-BC27-4576-9F4D-7253433319AA" with parameter Code
    end tell
end run