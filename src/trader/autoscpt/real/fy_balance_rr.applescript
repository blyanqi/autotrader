-- tell block to fy login
tell application "Keyboard Maestro Engine" 
    activate
    set kmValue to value of variable "set"
    do script "9B89AF81-F21C-4779-83B2-1086D4736747"
end
return [kmValue]