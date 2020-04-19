import React, { Component }  from 'react';
import CategoryButton from './CategoryButton';
import './App.css';
import './CategoryBar.css';

const categories = ["family-friendly", "artsy", "delicious", "geeky", "historic", "indoors", "outdoors", "romantic", "sporty"];

class CategoryBar extends Component {
    constructor(props) {
        super(props);
        this.state = new Map(categories.map(cat => [cat, false]));
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick= (category) => {
        this.setState((state) => ({
            [category]: !state[category]
         }));
    }

    render() {
        const categoryButtons = categories.map(category => (
            <CategoryButton
                key={category}
                category={category}
                onClick={this.handleClick}
                value={this.state[category]}
            />
        ));
        return (
            <div className="category-bar-scroll-filter">
                {categoryButtons} 
            </div>
        );
    }
}

export default CategoryBar;
