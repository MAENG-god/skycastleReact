import './App.css';
import {Route, Routes} from 'react-router-dom'
import Home from './pages/Home';
import Students from './pages/Students';

function App() {
  return (
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='/management/students' element={<Students />}/>
    </Routes>
  );
}

export default App;
