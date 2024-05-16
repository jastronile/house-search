import React, { useEffect, useState } from 'react'
import ReactMapGl, { Marker } from 'react-map-gl';
import "mapbox-gl/dist/mapbox-gl.css"
import { useLocation } from 'react-router-dom';
import axios from 'axios';

const Token="pk.eyJ1IjoicHJhdGhhbWVzaHNoaW5kZTA4IiwiYSI6ImNsdjJvYWhxajBneXgycnA4d3R3eTBjd3kifQ.zS3ixbQ1FjP0PoSIehbSKQ";
const Map = () => {
  const location=useLocation();
  
 const [lat,setLat]=useState(null);
 const [lon,setLon]=useState(null);
  useEffect(() => {
      // Ensure location.state.loc is not null before calling setUserData
      if (location.state && location.state.lat && location.state.lon) {
        setLat(location.state.lat);
        setLon(location.state.lon);

        
      }
    }, [location.state]); 

   console.log(lat);
   console.log(lon)
 
  

  const [viewport,setViewPort]=useState({latitude:18.4690,longitude:73.8641,zoom:11})
  const [data,setData]=useState(null);
  var marker_len=0;
  useEffect(() =>{
    const fetchData =async () =>{
        try{
            const response=await axios.get("http://localhost:5000/amenities");
            setData(response.data);
            marker_len=data.length;
        }
        catch(error)
        {
            console.log(error);
        }
    };
    fetchData();
 },[])


  var marker_len=data?.length;
  console.log(data)
   

  useEffect(() => {
    // Update viewport when lat and lon change
    if (lat && lon) {
      setViewPort((prevViewport) => ({
        ...prevViewport,
        latitude: lat,
        longitude: lon
      }));
    }
  }, [lat, lon]);
  return (
    <div style={{width:"100vw",height:"100vh"}}>
         <ReactMapGl
         {...viewport}
         mapboxAccessToken={Token}
         width="100%"
         height="100%"
         mapStyle='mapbox://styles/mapbox/streets-v12'
         onViewportChange={(viewport) => setViewPort(viewport)}
         >

          {lat&&lon?(
          <>
           
          <Marker
           latitude={lat}
           longitude={lon}
           >

          </Marker>
          
          </>)
          
          :null}

          {data && marker_len>0?(<> 
           {data.map((marker,index) =>(
              <Marker
              key={index}
               latitude={marker.Latitude}
               longitude={marker.Longitude}
              ></Marker>

           ))}

         </>):null

          }
    </ReactMapGl>
    </div>
  )
}

export default Map;