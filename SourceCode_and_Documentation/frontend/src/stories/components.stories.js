import React from 'react';
import { MoodButton as MoodButtonImpl } from '../MoodButton';
import { CovidDialog as CovidDialogImpl } from '../CovidDialog';
import { optionsKnob as options, withKnobs } from '@storybook/addon-knobs';
import { action } from '@storybook/addon-actions';
import '../App.css';

export default {
    title: 'Components',
    decorators: [withKnobs]
};

const moods = {
    delicious: "delicious",
    artsy: "artsy",
    sporty: "sporty",
    romantic: "romantic",
    outdoors: "outdoors",
    indoors: "indoors",
    geeky: "geeky",
    historic: "historic",
    "family-friendly": "family-friendly",  
}

export const CovidDialog = () =>
    <CovidDialogImpl />;

export const MoodButton = () =>
    <MoodButtonImpl
        mood={options('Mood', moods, 'delicious', { display: 'inline-radio' })}
        onClick={action('onClick')}
    />;
