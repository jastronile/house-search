import React, { useCallback, useState } from 'react'
import {AddressAutofill,useAddressAutofillCore} from '@mapbox/search-js-react';


const SearchBox = () => {
  const [location,setLocation]=useState('');
  const Token="pk.eyJ1Ijoic2FtZWVyNSIsImEiOiJjbGV2YnYxbWQwbXQ2M3Zta2tvM3ByMjdoIn0.dPW1SvG9F65_qCsdkgAt9w";
const handleSubmit=(e) =>{
  e.preventDefault();
   console.log(e.target[0].value)

}

const handleRetreive = useCallback ((place) =>{
  console.log("Oucch")
},[])
  return (
    <div> 
    
        <form  onSubmit={handleSubmit}>
        <label className="txt-s txt-bold color-gray mb3">Address</label>  
        <AddressAutofill accessToken={Token} onRetrieve={handleRetreive}>
        <input
        className="input mb12"
        placeholder="Start typing your address, e.g. 123 Main..."
        autoComplete="address-line1"
        id="mapbox-autofill"
        value={location}
        onChange={(e)=>setLocation(e.target.value)}
        
        />
      </AddressAutofill>
      <button type="submit" className="btn round" id="btn-confirm" >
Confirm
</button>
        </form>

    </div>
  )
}

export default SearchBox