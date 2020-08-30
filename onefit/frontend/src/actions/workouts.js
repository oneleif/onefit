import axios from "axios";

import { GET_WORKOUTS, DELETE_WORKOUT, ADD_WORKOUT } from "./types";

// GET WORKOUTS
export const getWorkouts = () => (dispatch) => {
  axios
    .get(`/api/workouts/`)
    .then((res) => {
      dispatch({
        type: GET_WORKOUTS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};

// DELETE WORKOUT
export const deleteWorkout = (id) => (dispatch) => {
  axios
    .delete(`/api/workouts/${id}/`)
    .then((res) => {
      dispatch({
        type: DELETE_WORKOUT,
        payload: id,
      });
    })
    .catch((err) => console.log(err));
};

// ADD WORKOUT
export const addWorkout = (workout) => (dispatch) => {
  axios
    .post(`/api/workouts/`, workout)
    .then((res) => {
      dispatch({
        type: ADD_WORKOUT,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
