import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'

function RouterApp() {
    return(
        <BrowserRouter>
            <nav>

            </nav>

            <Routes>
                <Route path="/"/>
                <Route path='/login'/>
            </Routes>


        </BrowserRouter>
    );
}

export default RouterApp