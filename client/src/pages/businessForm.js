import React, { useEffect, useState } from 'react'
import './businessform.css'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function BusinessForm() {
  const [businessData,setBusinessData]=useState({business_name:"",business_type:"",keywords:""});
  const navigate=useNavigate();
  const [data,setData]=useState();
  function handleChange(e)
  {
    let {name,value}=e.target;
      setBusinessData({...businessData,[name]:value});

  }

  function HandleSubmit(e)
  {
    e.preventDefault();
    try {
      axios({
        method:'POST',
        url:'http://localhost:5000/business',
        data:{
          business_name:businessData.business_name,
          business_type:businessData.business_type,
          keywords:businessData.keywords,
        }
      })
      
    } catch (error) {
      console.log(error)
    }
  
     navigate("/map");


  }
  return (
    <div>
      <div className='text-center text-2xl font-bold mt-10'> Kindly Fill the Business Form </div>
       <form onSubmit={HandleSubmit} className='business_form'>
       <label  className='label'>Business Name: </label>
        <input type='text' className='input' name="business_name"  onChange={handleChange}/><br/>
        <label  className='label'>Business Type: </label>
        <input type='text' className='input' name="business_type"  onChange={handleChange}/><br/>
        <label  className='label'>Enter Keywords: </label>
        <input type='text' className='input' name="keywords"  onChange={handleChange}/><br/>
        <input type='submit' value="Submit" className='button'></input>
       </form>
    </div>
  )
}
