import React, {useEffect, useState} from 'react'; 
  function Timer() { 
    const [seconds, setSeconds] = useState(0) 
      useEffect(() => { 1000) // wrong syntax , should appear at the end of setInterval funcation
        const interval = setInterval(() => {setSeconds(seconds + 1)},  // Not using previous state , it will not update
          return() => clearTimeout(interval) }, []) // should use clearInterval
      return <div>Time: {seconds} seconds</div> 
} 





// correct one 
import React, {useEffect, useState} from 'react'; 
function Timer() { 
    const [seconds, setSeconds] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {
            setSeconds(prevSecond => prevSecond + 1);
        }, 1000);

        return() => clearInterval(interval);
    }, []) 
    return <div>Time: {seconds} seconds</div> 
} 
