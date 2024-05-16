import React, { useState ,useEffect } from 'react'
import { useLocation } from 'react-router-dom';

export default function UserLocation() {
    const location=useLocation();
    const [userdata,setUserData]=useState(null);
    useEffect(() => {
        // Ensure location.state.loc is not null before calling setUserData
        if (location.state && location.state.loc) {
          setUserData(location.state.loc);
          
        }
      }, [location.state]); 

      console.log(userdata);
  return (
    <div>UserLocation</div>
  )
}
