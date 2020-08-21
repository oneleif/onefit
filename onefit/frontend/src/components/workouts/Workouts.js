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
        {/* example table */}
        <h2>Workouts</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Message</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.workouts.map((workout) => (
              <tr key={workout.id}>
                <td key={workout.id}></td>
                <td key={workout.name}></td>
                <td key={workout.email}></td>
                <td key={workout.message}></td>
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
