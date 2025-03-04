-- tell block to fy buy
tell application "Keyboard Maestro Engine" 
    activate
    set kmValue to value of variable "holdInfo"
    do script "94D240F0-C07A-493F-8856-FB79B34639B4"
end tell
return kmValue