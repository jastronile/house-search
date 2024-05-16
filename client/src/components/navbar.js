import React from 'react'
import { Link, NavLink } from  "react-router-dom";
import "./navbar.css"


const Navbar = () => {
  return (
 <>
    <div>
      <div className='container'>
         <div className='text-xl font-semibold'>Spell-Bound Properties</div>
      <div className='navbar'>
         <Link to='/'>
         <div className='text-xl hover:font-semibold'>Home</div> 
         </Link>
         <Link to='/map'>
         <div className='text-xl hover:font-semibold'>Map</div> 
         </Link>
         <Link to='/form'>
        <div className='text-xl hover:font-semibold'>Form</div> 
        </Link>
        <Link to='/showlocation'>
        <div className='text-xl hover:font-semibold'>Places</div> 
        </Link>
        <Link to='/businessForm'>
        <div className='text-xl hover:font-semibold'>Businessform</div> 
        </Link>
        </div>
        </div>
    </div>
  
    </>
  )
}

export default Navbar