import './App.css';
import Map from './pages/Map'
import SearchBox from './components/SearchBox';
import Home from './pages/Home';
import Form from "./pages/form";
import Navbar from './components/navbar';
import { BrowserRouter,Route,Routes } from 'react-router-dom';
import Excel from './pages/excel';
import UserLocation from './pages/userLocation';
import Showlocation from './pages/showlocation';
import UserFeedback from './pages/userFeedback';
import BusinessFom from './pages/businessForm';
import BusinessForm from './pages/businessForm';


function App() {
  return (
   
    <>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/map" element={<Map/>}/>
        <Route path="/form" element={<Form/>}/>
        <Route path="/excel" element={<Excel/>}/>
        <Route path ="/userLocation" element={<UserLocation/>}/>
        <Route path="/ShowLocation" element={<Showlocation/>}/>
        <Route path="/userFeedback" element={<UserFeedback/>}/>
        <Route path='/businessForm' element={<BusinessForm/>}/>
      </Routes> 
  
    
    </>
   
 
  );
}

      {/* <div className="input">
        <h1 className='heading'>House Search</h1>
       <SearchBox/>
      </div>
          <Map/> */}

export default App;
