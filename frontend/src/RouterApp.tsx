import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './pages/login/login';
import Register from './pages/register/register';
import { Room } from './pages/room/room';

function RouterApp() {
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/"/>
                <Route path='/login' element={<Login/>}/>
                <Route path='/register' element={<Register/>}/>
                <Route path='/room' element={<Room/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default RouterApp
