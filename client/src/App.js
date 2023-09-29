import './App.css';
import volunteer from './volunteer.js';
import './user.js';
import admin from  './admin.js' ;
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";

import './App.css';
import User from './user.js';


function App() {
  return (
    <div className="App">
      <header className="App-header">

        <p>
          Select Page
        </p>

       <Router>
          {/* <Link to='/'>Select User Type</Link> */}
          <Link to='/user'>General Member</Link>
          <Routes>
            <Route path='/user' element={<User/>} />
            {/* <Route path='/about' element={<About/>} /> */}
          </Routes>
         {/* <Switch>
           <Route path="/user"
                component={user}/>
            <Redirect to="/" />
         </Switch> */}
       </Router>

      </header>
    </div>
  );
}

export default App;
