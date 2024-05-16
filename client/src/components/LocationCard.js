import React from 'react'
import houseimg from '../images/house.jpg'
import { useNavigate } from 'react-router-dom'


export default function LocationCard(props) {
   
   const cluster=new Map([
    ["0","Most Suitable"],
    ["1","Neutral"],
    ["2","Not Suitable"]
   ])
    //  console.log(props.data.Apartment_Longitude)
    const navigation=useNavigate()
function handleClick()
{
    navigation("/map",{state:{lat:props.data.Apartment_Latitude,lon:props.data.Apartment_Longitude}})
     
}
  return (
    <div className=' w-fit border border-gray-900 p-5 rounded-lg shadow-xl m-5 hover:cursor-pointer'>
        <div className=' flex flex-col justify-center'>
            <div className='flex flex-col'>
           <div className='font-bold text-2xl'>{props.data.Apartment_Name}
           </div>
           <div className='text-sm text-zinc-800 m-1'>{props.data.Apartment_Location}</div>
           </div>
           <div className='flex flex-row justity-around gap-20 items-center'>
        
            <div>
               <img src={houseimg} height={300} width={350}></img>
            </div>
            <div className='flex flex-col gap-7'>
                <div className='flex flex-row gap-3'>

                <span>
               <div className='flex flex-col'>
                <div className='font-bold text-md'>Deposit
               </div>
                 <div className='text-sm m-2'>{props.data.Apartment_Deposit}</div>
                     </div>
            </span>

                {/* rent  */}
          <span>
                <div className='flex flex-col'>
                    <div className='font-bold text-md'>Rent
                </div>
                    <div className='text-sm '>{props.data.Apartment_Rent}</div>
                    </div>
           </span>
          {/* Deposit  */}
           
                </div>
                
                <div className='flex flex-row gap-3'>
                    {/* Negotiable */}
               <span>
               <div className='flex flex-col'>
                <div className='font-bold text-md'>Negotiable
               </div>
                 <div className='text-sm'>{props.data.Apartment_Negotiable}</div>
                     </div>
              </span> 
              {/* Cluster */}
               <span>
               <div className='flex flex-col'>
                <div className='font-bold text-md'>Flat
               </div>
                 <div className='text-sm'>{cluster.get(String(props.data.Cluster))}</div>
                     </div>
                </span> 
                </div>
                <button onClick={()=> handleClick()} className='w-fit  h-fit border p-2 rounded-2xl border-slate-700 bg-sky-400 text-white font-md hover:bg-sky-600'>Show on maps</button>
            </div>
            </div>
         
        </div>
    </div>
  )
}
