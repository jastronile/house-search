import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { featured } from '../data';
import LocationCard from '../components/LocationCard';
import './location.css' 
import houseicon from "../images/houseicon.png";
import { useNavigate } from 'react-router-dom';


export default function Showlocation() {

    const [userdata,setUserData]=useState([]);
    const navigate=useNavigate();

     useEffect(() =>{
        const fetchData =async () =>{
            try{
                const response=await axios.get("http://localhost:5000/getdata");
                setUserData(response.data);
            }
            catch(error)
            {
                console.log(error);
            }
        };
        fetchData();
     },[])
   
     
    function handleClick()
    {
        navigate("/userFeedback")
    }
   
  return (
   userdata.length==0?<div className='text-center font-bold text-xl m-5'>No House available ;</div>:
    <div>
        <div className='flex flex-row justify-center mt-5'> 
        <h1 className='text-center text-3xl mt-2'>Houses</h1>
        <img src={houseicon} height={50} width={50}></img>
        </div>
        <div className='flex flex-row justify-end mr-20'>
        <button className='w-fit h-fit border border-black bg-amber-300 font-semibold p-2 rounded-lg' onClick={()=>handleClick()}>FeedBack</button>
        </div>
        {
         userdata.map((item) => (
            <div className='location-container'>
                <LocationCard
                  data={item}
                />
            </div>
         )) 
      
}
    </div>
  )

}
