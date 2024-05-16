import React from 'react'
import { useState } from 'react';
import './form.css'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Form = () => {
  const [userdata,setData]=useState({Full_name:"",city:"",gender:"",age:0,occupation:"",budget:0,area:"",pref:""});
  const navigate=useNavigate();


  function handleSubmit(e)
  {
    e.preventDefault();
    console.log(userdata);

     
    try{
      axios({
        method:'POST',
        url:'http://localhost:5000/',
        data:{
          Full_name:userdata.Full_name,
          city:userdata.city,
          gender:userdata.gender,
          age:userdata.age,
          occupation:userdata.occupation,
          budget:userdata.budget,
          area:userdata.area,
          pref:userdata.pref
        }
      })
    }
    catch(err)
    {
      console.log(err);
    }
   
     
     navigate("/ShowLocation");
  
  }


  function handleChange(e)
  {
    e.preventDefault();
     let {name,value}=e.target;
     let v=e.target.id;
     name=='area'?setData({...userdata,[name]:v}):setData({...userdata,[name]:value});
    
  }
  return (
    <div className='mainContainer'>
      <h1 className='heading'>Kindly fill the form</h1>
      <div>
      <form className='form' id='userform' name='userform' onSubmit={handleSubmit}>
        <label  className='label'>Full Name: </label>
        <input type='text' className='input' name="Full_name"  onChange={handleChange}/><br/>

        <label className='label' >City: </label>
        <input type='text' className='input' name='city' onChange={handleChange}/><br/>

        <label className='label' >Gender </label>
        <input type='text' name='gender'className='input' onChange={handleChange}/><br/>

        <label className='label'>Age</label>
        <input type='number' name='age'className='input'onChange={handleChange}/><br/>

        <label className='label'>Occupation: </label>
        <input type='text' className='input' name='occupation' onChange={handleChange}/><br/>

        <label className='label'>Budget permonth(Rs): </label>
        <input type='text' className='input' name='Budget' onChange={handleChange}/><br/>
        
        <label className='label'>Area :</label><br/>
        <input type='radio' name='area' id='Western' onChange={handleChange}/>
        <label for="area1" className='p-2'>Western</label>
        <input type='radio' name='area' id='Central' onChange={handleChange}/>
        <label for="area2"  className='p-2'>Central</label>
        <input type='radio' name='area' id='Northern' onChange={handleChange}/>
        <label for="area3" className='p-2'>Northern</label>
        <input type='radio' name='area' id='Eastern' onChange={handleChange}/>
        <label for="area4" className='p-2'>Eastern</label>
        <input type='radio' name='area' id='Southern' onChange={handleChange}/>
        <label for="area5" className='p-2'>Southern</label><br/><br/>
        
        

        <label className='label'>Describe your preferences:</label><br/>
         <textarea rows="6" cols="48" className='input' method="post"  name='pref' onChange={handleChange}></textarea><br/>
        <input type='submit' value='Submit' className='button'></input>
      </form>
      </div>
    
    </div>
  )
}

export default Form