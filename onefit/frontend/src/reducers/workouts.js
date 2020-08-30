import { GET_WORKOUTS, DELETE_WORKOUT, ADD_WORKOUT } from "../actions/types.js";

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
    case DELETE_WORKOUT:
      return {
        ...state,
        workouts: state.workouts.filter(
          (workout) => workout.id !== action.payload
        ),
      };
    case ADD_WORKOUT:
      return {
        ...state,
        workouts: [...state.workouts, action.payload],
      };
    default:
      return state;
  }
}
