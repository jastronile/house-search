import React, { useState } from 'react'
import * as xlsx from 'xlsx'
import { useNavigate} from 'react-router-dom';


export default function Excel() {

     const [houseData,setHouseData]=useState();
    
        const readExcel=async(e)=>{
        const file=e.target.files[0];
        const data= await  file.arrayBuffer(file);
        const excelfile=xlsx.read(data);
        const excelSheet=excelfile.Sheets[excelfile.SheetNames[0]];
        const exceljson=xlsx.utils.sheet_to_json(excelSheet)
        setHouseData(exceljson)
        }

        const navigate=useNavigate();

        function handleClick()
        {
        
            navigate('/map',{state:{loc:houseData}})
               
        }
    
  return (
    <div>
     <p className='pt-5 pb-5  pl-2 text-lg'>Upload the excel File</p>
     <input type='file' onChange={(e) =>readExcel(e)}></input>
     <button type='submit' className='w-16 h-10 bg-fuchsia-500 rounded-md' value='Submit' onClick={() =>handleClick()}>Submit</button>
    </div>
  )
}
