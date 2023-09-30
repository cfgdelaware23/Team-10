import React from 'react';
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <p>Welcome to the Homepage!</p> {}
      <nav>
        <Link to='/members'>General Member</Link>
      </nav>
      <nav>
        <Link to='/Display'>Display Page</Link>
      </nav>
    </div>
  );
}

export default Home;