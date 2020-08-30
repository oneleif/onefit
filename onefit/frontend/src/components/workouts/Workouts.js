import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getWorkouts, deleteWorkout } from "../../actions/workouts";

export class Workouts extends Component {
  static propTypes = {
    workouts: PropTypes.array.isRequired,
    getWorkouts: PropTypes.func.isRequired,
    deleteWorkout: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.getWorkouts();
  }

  render() {
    return (
      <Fragment>
        <h2>Workouts</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>date</th>
              <th>notes</th>
              <th>username</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.workouts.map((workout) => (
              <tr key={workout.id}>
                <td>{workout.id}</td>
                <td>{workout.date}</td>
                <td>{workout.notes}</td>
                <td>{workout.user_name}</td>
                <td>
                  <button
                    onClick={this.props.deleteWorkout.bind(this, workout.id)}
                    className="btn btn-danger btn-sm"
                  >
                    {" "}
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  workouts: state.workouts.workouts,
});

export default connect(mapStateToProps, { getWorkouts, deleteWorkout })(
  Workouts
);
