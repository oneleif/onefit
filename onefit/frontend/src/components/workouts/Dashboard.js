import React, { Fragment } from "react";
import Form from "./Form";
import Workouts from "./Workouts";

export default function Dashboard() {
  return (
    <Fragment>
      <Form />
      <Workouts />
    </Fragment>
  );
}
