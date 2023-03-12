import React from 'react';
import {Route, Switch} from "react-router-dom";
import Start from "./pages/start/Start";
import Login from "./pages/login/Login";
import SetFilters from "./pages/setFilters/SetFilters";

const Routing = () => {
    return (
        <Switch>
            <Route component={Start} path='/' exact/>
            <Route component={Login} path={'/login'} exact/>
            <Route component={SetFilters} path={'/set-filters'} exact/>
        </Switch>
    );
};

export default Routing;