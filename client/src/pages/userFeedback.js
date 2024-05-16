import React, { useState } from 'react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function UserFeedback() {
    const [feedback,setfeedback]=useState("");
    const navigate= useNavigate();
    function handleChange(e)
    {
        e.preventDefault();
         let {value}=e.target;
         setfeedback({...feedback,value});

    }

    function handleSubmit(e)
    {
        e.preventDefault();
        try {
            axios({
                method:'POST',
                url:"http://localhost:5000/feedback",
                data:{feedback}
                
            })
            
        } catch (error) {
             console.log(error)
        }

        alert("Thank you for your Feedback :)")
        navigate("/")
        
        
    }
  return (
    <div className='text-center m-10'>
        
        <label className='text-2xl'>Give Feedback</label><br/>
         <textarea rows="10" cols="50" className='input' name='feedback'onChange={handleChange}></textarea><br/>
         <button onClick={handleSubmit} className='w-fit h-fit p-2 border rounded-xl bg-sky-500'>Submit</button>
         
    </div>
  )
}
