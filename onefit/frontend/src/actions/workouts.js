import axios from "axios";

import { GET_WORKOUTS } from "./types";

// GET WORKOUTS
export const getWorkouts = () => (dispatch) => {
  axios
    .get("/api/workouts/")
    .then((res) => {
      dispatch({
        type: GET_WORKOUTS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
