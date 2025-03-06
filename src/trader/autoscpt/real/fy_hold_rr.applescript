-- tell block to fy buy
tell application "Keyboard Maestro Engine" 
    activate
    set kmValue to value of variable "holdInfo"
    set kmValue1 to value of variable "rate"
    set kmValue2 to value of variable "zset"
    do script "94D240F0-C07A-493F-8856-FB79B34639B4"
end tell
return [kmValue,kmValue1]