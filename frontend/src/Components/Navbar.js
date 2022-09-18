import logo from '../require/logo-black.png';

function Navbar() {
    return (
      <nav className="Navbar">
        <img src={logo} alt="logo" />
        <h1>Home</h1>
        <h1>Location</h1>
        <div className="nav--button">
        <button class="btn btn-dark">Reserve</button>
        <button class="btn btn-dark">Login</button>
        </div>
      </nav>
    );
  }
  
  export default Navbar;