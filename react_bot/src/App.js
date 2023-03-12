import './App.css';
import Routing from "./Routing";
import {createContext, useContext} from "react";

function App() {
    const DataContext = createContext([])
    return (
        <div className="App">
            <DataContext.Provider>
                <Routing/>
            </DataContext.Provider>
        </div>
    );
}


export default App;
