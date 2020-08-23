import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getWorkouts } from "../../actions/workouts";

export class Workouts extends Component {
  static propTypes = {
    workouts: PropTypes.array.isRequired,
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
              <th>date created</th>
              <th>notes</th>
              <th>username</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.workouts.map((workout) => (
              <tr key={workout.id}>
                <td>{workout.id}</td>
                <td>{workout.date_created}</td>
                <td>{workout.notes}</td>
                <td>{workout.user_name}</td>
                <td>
                  <button className="btn btn-danger btn-sm">Delete</button>
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

export default connect(mapStateToProps, { getWorkouts })(Workouts);
