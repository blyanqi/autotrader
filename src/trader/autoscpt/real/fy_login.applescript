-- tell block to fy login
try
    tell application "Keyboard Maestro Engine" 
        activate
        do script "90BD937C-9AC1-45C9-85C3-28BA896B017D"
    end
on error 
    return false
end try