import { GET_WORKOUTS } from "../actions/types.js";

const initialState = {
  workouts: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_WORKOUTS:
      return {
        ...state,
        workouts: action.payload,
      };
    default:
      return state;
  }
}
