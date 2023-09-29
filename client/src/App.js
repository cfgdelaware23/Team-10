import './App.css';
import volunteer from './volunteer.js';
import user from './user.js';
import admin from  './admin.js' ;
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import './App.css';





function App() {
  return (
    <div className="App">
      <header className="App-header">
      
        <p>
          Select Page

        </p>
        
       <Router>
         <Switch>
           <Route exact path="/user"
                component={user}/>
            <Route exact path="/admin"
                component={admin}/>

         </Switch>
       </Router>
        
      </header>
    </div>
  );
}

export default App;
